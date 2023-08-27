import modules.draw_crosses as m_cross
import modules.draw_circle as m_zero
import modules.data_base as m_data
import modules.who_victory as m_victory

def who_turn(x, y, number):
    if m_data.step[0] == "cross" and m_data.list_cell[number] == 0:
        rd = (x ,y)
        ld = (x-100 ,y)
        rt = (x,y-100)
        lt = (x-100,y-100)
        m_cross.draw_crosses(lt,ld,rt,rd)
        m_data.list_cell[number] = 1
        m_data.step[0] = "zero"
        m_victory.victory(1)
        if len(m_data.step) >= 2:
            m_data.step[1] = 'cross'
        else:
            m_data.step.append('cross')
    elif m_data.step[0] == "zero" and m_data.list_cell[number] == 0:
        x,y = x- 50,y- 50
        m_zero.draw_circle(x,y)
        m_data.list_cell[number] = 2
        m_data.step[0] = "cross"
        m_victory.victory(2)
        if len(m_data.step) >= 2:
            m_data.step[1] = 'zerro'
        else:
            m_data.step.append('zerro')